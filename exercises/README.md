# Kathará Exercises

This section contains a set of Kathará exercises whose solution can be automatically checked using
the `kathara-lab-checker` tool.
These exercises are designed to help users become familiar with network emulation, protocol configurations, and
network troubleshooting using the Kathará network emulation tool.

Each folder in this section represents a standalone exercise with its own configuration files, instructions, and
expected output.

## Prerequisites

Before working on these exercises, you need to have the following installed:

- [Docker](https://www.docker.com/)
- [Kathará](https://www.kathara.org/)
- [Python3.11](https://www.python.org/downloads/) or higher.

## Installation

### Set up a Virtual Environment (Recommended)

To avoid conflicts with system-wide Python dependencies, it’s recommended to create and use a virtual environment before
installing the kathara-lab-checker tool.

```bash
python3 -m venv kathara-labs-venv
```

**NOTE**: The Python version MUST be `>=3.11`.

Then, activate the virtual environment:

On Linux/macOS:

```bash
source kathara-labs-venv/bin/activate
```

On Windows

```bash
kathara-labs-venv\Scripts\activate
```

### Install the kathara-lab-checker Tool

Once the virtual environment is active, install the `kathara-lab-checker` tool from PyPI:

```bash
pip install kathara-lab-checker
```

The kathara-lab-checker tool will allow you to automatically validate your solutions to the exercises by comparing the
actual network state against the expected results.

## Getting Started

You are ready to dive into Kathará exercise. Each exercise is self-contained and provides all the information to
complete it and automatically check the results.
