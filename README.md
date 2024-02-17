[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![CI](https://github.com/snapp-incubator/prom-reporter/actions/workflows/ci.yml/badge.svg)](https://github.com/snapp-incubator/prom-reporter/actions/workflows/ci.yml)
[![RELEASE](https://github.com/snapp-incubator/prom-reporter/actions/workflows/release.yml/badge.svg)](https://github.com/snapp-incubator/prom-reporter/actions/workflows/release.yml)

# Prom Reporter

This repo provides a reporter to gather insight from desired prometheus metrics.

## Requirements

- Python 3.12+

## Installation

```sh
pip install -r requirements.txt
```

## Usage

1. Create a config yaml file containing your desired queries just like the [repo example](tests/config.yaml).
2. Run the application providing the config and the output files' paths:

    ```sh
    python app/main.py -c tests/config.yaml -o output.json
    ```

## Contributing

Thank you for considering contributing! If you find an issue or have a better way to do something, feel free to open an issue or a PR.

### Test

```sh
pytest -v
```

### Coverage

```bash
coverage run -m pytest
coverage report
```

## License

This repository is open-sourced software licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
