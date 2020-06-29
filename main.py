from rnn.biLSTM_inference import biLSTM_inference
from numpy import load
from torch import from_numpy


def main():
    data = load('training_data/MIMIC_MV_data.npy')

    # example for a single instance (shape: [seq_size, feature_size])
    input = from_numpy(data[0])

    # # ezample for multiple instances in tensor
    # # (shape: [batch_size, seq_size, feature_size])
    # input = from_numpy(data[0:10])

    time = '20200115-194901'
    best_epoch = 46
    best_accuracy = 0.96
    filepath = 'model/'
    model = biLSTM_inference(filepath, time, best_epoch, best_accuracy)
    result = model.predict(input)
    print('the prediction result:', result)


if __name__ == "__main__":
    main()
