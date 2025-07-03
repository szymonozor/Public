# Python Project: Sample Application

Description: A simple Python application for educational purposes.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Installation

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Sample code:
```python
print("Hello, world!")
```

## Deployment

### CI/CD Workflow
- Automatic tests and linting on every push and pull request (GitHub Actions)
- Docker image built on CI
- Automatic deployment to server after successful tests on main branch
- Health check endpoint: `/health`
- Rollback in case of failed deployment

### How to deploy manually
1. Build Docker image:
   ```sh
   docker build -t my-python-app .
   ```
2. Run:
   ```sh
   docker run -d -p 8000:8000 my-python-app
   ```
3. Health check:
   Visit [http://localhost:8000/health](http://localhost:8000/health) (should return OK)

### Environment configuration
- Secrets managed via GitHub Actions secrets (e.g. SSH_PRIVATE_KEY)
- Environment variables loaded from `.env` file or repository secrets

## Example Table

| File        | Description            |
|-------------|-----------------------|
| main.py     | Main application file  |
| README.md   | Documentation         |
| Dockerfile  | Docker build config   |
| requirements.txt | Python dependencies |
| .github/workflows/ci.yml | CI workflow |
| .github/workflows/cd.yml | CD workflow |

## Links
- [Python](https://www.python.org/)
- [GitHub](https://github.com/)

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Project under the MIT license. See [LICENSE](LICENSE) for details. 

## Features

12345
