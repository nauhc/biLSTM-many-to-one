<!-- Thanks https://github.com/othneildrew/Best-README-Template
    for the README Template -->
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- [![Contributors][contributors-shield]][contributors-url] -->
<!-- [![Forks][forks-shield]][forks-url] -->
<!-- [![Stargazers][stars-shield]][stars-url] -->

[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!-- <a href="https://github.com/github_username/repo">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">biLSTM_many_to_one</h3>

  <p align="center">
    Providing an biLSTM many-to-one model (PyTorch) with attention mechanism
    <br />
    Inference with pretrained biLSTM model for sequence predictions
    <br />
    <!-- <a href="https://github.com/github_username/repo"><strong>Explore the docs »</strong></a>
    <br /> -->
    <br />
    <!-- <a href="https://github.com/nauhc/biLSTM-many-to-one">View Demo</a> -->
    ·
    <a href="https://github.com/nauhc/biLSTM-many-to-one/issues">Report Bug</a>
    ·
    <a href="https://github.com/nauhc/biLSTM-many-to-one/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
  <!-- - [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements) -->

<!-- ABOUT THE PROJECT -->

## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

<!-- Here's a blank template to get started: -->
<!-- **To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`github_username`, `repo`, `twitter_handle`, `email` -->

<!-- ### Built With

- []()
- []()
- []() -->

<!-- GETTING STARTED -->

This repo provides an biLSTM many-to-one model implemented in PyTorch.
An wrapper program for predictions/inferences using a trained biLSTM is also included. The result returns the probabilities of each class.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

<!-- This is an example of how to list things you need to use the software and how to install them.

- npm

```sh
npm install npm@latest -g
``` -->

- Python 3 (Python 2 is no longer supported by the Python Software Foundation.)
- PyTorch
- Numpy

### Installation

<!-- 1.  Clone the repo -->

```sh
git clone https://github.com/nauhc/biLSTM-many-to-one.git
```

<!-- 2.  Install NPM packages

```sh
npm install
``` -->

<!-- USAGE EXAMPLES -->

## Usage

<!-- Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_ -->

1.  Clone the repo to your local directory
2.  If using the example in main.py:
    - Add the pre-trained biLSTM model to the root directory: create a 'model' directory and put pretrained models inside
    - Add data for inference: create a 'data' directory, and put data (numpy format) inside
    - Change the [time, epoch, accuracy] parameter in main.py to local a particular model
    - Change the parameters in rnn/parameter.py if trained using alternative parameters
3.  Ready to go! Run the main.py and see the predition results!

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/nauhc/biLSTM-many-to-one/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

<!-- ## Contact -->

<!-- Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email -->

<!-- Project Link: [https://github.com/github_username/repo](https://github.com/github_username/repo) -->

<!-- ACKNOWLEDGEMENTS -->

<!-- ## Acknowledgements -->

<!-- - []()
- []()
- []()
 -->
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
