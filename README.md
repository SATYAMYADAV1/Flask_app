# Flask App

This project is a simple Flask application with a basic route and automated tests. It was set up as a small learning project to understand:

- Python Flask app structure
- pytest-based testing
- GitHub Actions CI workflow
- Docker image build setup
- pushing code to GitHub

## Project overview

The app is defined in [Pyth_prac.py](Pyth_prac.py). It exposes a home route and a name-based route.

Example routes:

- `/` -> returns `Hello, Flask!`
- `/greet/Satya` -> returns `Hello, Satya!`

## Local setup

1. Create and activate a virtual environment (optional but recommended)
2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

3. Run the app

```bash
python Pyth_prac.py
```

4. Open in browser:

```text
http://localhost:5000/
```

## Running tests

```bash
pytest -q
```

This validates the app behavior and ensures the routes work as expected.

## CI workflow

The project includes a GitHub Actions workflow in [.github/workflows/ci.yml](.github/workflows/ci.yml) that:

- checks out the repository
- sets up Python 3.12
- installs dependencies
- runs the test suite with `pytest`
- builds the Docker image

This ensures the code is validated automatically on pushes and pull requests to the `main` branch.

## Docker setup

A Dockerfile is included at [Dockerfile](Dockerfile) so the app can be built in CI or locally.

### Build the image locally

```bash
docker build -t flask-app .
```

### Run the container locally

```bash
docker run -p 5000:5000 flask-app
```

## GitHub flow used

The project was initialized locally, cleaned up, committed, and pushed to GitHub using Git commands like:

```bash
git add .
git commit -m "Initial Flask app setup"
git push origin main
```

This made the repository available on GitHub and allowed the CI workflow to run automatically.

## Summary

This project demonstrates a simple end-to-end workflow for a Flask app:

- write app code
- add tests
- run pytest locally
- create CI workflow
- build Docker image in CI
- push to GitHub

It is a practical example of how a small Python web app can be automated and validated in a real DevOps workflow.
