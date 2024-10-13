
$fileName = "installed"
$filePath = Join-Path -Path $PWD.Path -ChildPath $fileName
# Pa cuando se parta vite  Remove-Item -Path "node_modules\.vite\deps" -Recurse -Force

if (-not (Test-Path -Path $filePath)) {
    New-Item -ItemType File -Name $fileName -Force

    poetry run python manage.py makemigrations
    poetry run python manage.py migrate

    poetry run python manage.py loaddatautf8 fixtures/routes.json
    poetry run python manage.py loaddatautf8 fixtures/buses.json
    poetry run python manage.py loaddatautf8 fixtures/employees.json

}

poetry run python manage.py runserver
