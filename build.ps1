$exclude = @("venv", "bot_funcionarios.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_funcionarios.zip" -Force