# Contributing to URLCrafter

Thank you for considering contributing to URLCrafter! This document provides guidelines and instructions for contributing to the project.

Created by Madhav Panchal (2025).

## Code of Conduct

By participating in this project, you agree to abide by its Code of Conduct.

## How Can I Contribute?

### Reporting Bugs

- Check if the bug has already been reported in the Issues.
- Use the Bug Report template when creating a new issue.
- Include detailed steps to reproduce the bug.
- Include the Python version and URLCrafter version.
- Provide examples that demonstrate the bug.

### Suggesting Features

- Check if the feature has already been suggested in the Issues.
- Use the Feature Request template when creating a new issue.
- Provide a clear description of the feature.
- Explain how the feature would benefit the project.

### Pull Requests

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/amazing-feature`).
3. Make your changes.
4. Run the tests to ensure your changes don't break existing functionality.
5. Add or update tests as needed for your changes.
6. Update documentation to reflect any changes.
7. Commit your changes (`git commit -m 'Add some amazing feature'`).
8. Push to the branch (`git push origin feature/amazing-feature`).
9. Open a Pull Request.

## Development Setup

1. Clone your fork of the repository.
2. Install the project in development mode:
   ```
   pip install -e .
   ```
3. Install development dependencies:
   ```
   pip install pytest pytest-cov
   ```

## Running Tests

Run all tests:

```
pytest
```

Run tests with coverage:

```
pytest --cov=urlcrafter
```

## Coding Style

- Follow PEP 8 guidelines.
- Include docstrings for all public classes and methods.
- Use type hints where appropriate.
- Keep lines under 100 characters.

## Documentation

- Update the README.md if your changes affect the usage of the library.
- Add examples for new features.
- Update the docstrings for any modified code.

## Versioning

URLCrafter follows Semantic Versioning (SemVer):

- MAJOR version for incompatible API changes
- MINOR version for new functionality in a backwards compatible manner
- PATCH version for backwards compatible bug fixes

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License. 