from app import init_app  # pylint: disable=missing-module-docstring


app = init_app()

if __name__ == "__main__":
    app.run(host='18.223.201.179')
