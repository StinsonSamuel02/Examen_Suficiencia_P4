# Directorio actual
$currentDirectory = Get-Location

# Elimina el archivo 'installed'
Remove-Item -Path "$currentDirectory\installed" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$currentDirectory\db.sqlite3" -Force -ErrorAction SilentlyContinue
# Busca y elimina archivos terminados en '_temp'
#Get-ChildItem -Path $currentDirectory -Filter "*_temp*" -File | Remove-Item -Force -ErrorAction SilentlyContinue
