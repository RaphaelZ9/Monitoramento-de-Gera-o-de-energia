Set WshShell = CreateObject("WScript.Shell")

WshShell.Run """C:\MonitorGeracao\Iniciar Monitor de Geracao.bat""", 0, False

Set WshShell = Nothing