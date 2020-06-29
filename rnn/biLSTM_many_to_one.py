# bidirectional LSTM with attention outputs

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
from numpy import sqrt


class Attn(nn.Module):
    def __init__(self, hidden_size, batch_first=True):
        super(Attn, self).__init__()
        self.hidden_size = hidden_size
        self.batch_first = batch_first

        self.weights = nn.Parameter(torch.Tensor(hidden_size, 1))
        stdv = 1.0 / sqrt(self.hidden_size)
        for weight in self.weights:
            nn.init.uniform_(weight, -stdv, stdv)

    def forward(self, x):
        if self.batch_first:
            batch_size, seq_size = x.size()[:2]
        else:
            seq_size, batch_size = x.size()[:2]

        weights = torch.bmm(x, self.weights.unsqueeze(
            0).repeat(batch_size, 1, 1))

        attentions = torch.softmax(F.relu(weights.squeeze()), dim=-1)

        # apply attention weights
        weighted_input = torch.mul(
            x, attentions.unsqueeze(-1).expand_as(x))

        return weighted_input, attentions


class biLSTM_many_to_one(nn.Module):
    def __init__(self, batch_size, seq_size, feature_size, hidden_size, num_layers, out_size, use_gpu):
        super(biLSTM_many_to_one, self).__init__()
        self.use_gpu = use_gpu
        self.batch_size = batch_size
        self.seq_size = seq_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.lstm = nn.LSTM(input_size=feature_size,
                            hidden_size=hidden_size,
                            num_layers=num_layers,
                            batch_first=True,
                            bidirectional=True)
        self.hidden2label = nn.Linear(hidden_size * 2, out_size)
        self.hidden = self.initial_hidden()

        # attention layer
        self.attention = Attn(self.hidden_size * 2)

    def initial_hidden(self):
        return (Variable(torch.zeros(2, self.batch_size, self.hidden_size)).double(),
                Variable(torch.zeros(2, self.batch_size, self.hidden_size)).double())

    def forward(self, x):

        self.hidden = self.initial_hidden()

        lstm_out, self.hidden = self.lstm(x, self.hidden)

        # attention layer after LSTM
        attn_out, attns = self.attention(lstm_out)

        y = self.hidden2label(attn_out[:, -1, :].double())
        log_probs = nn.functional.log_softmax(y)
        return log_probs
