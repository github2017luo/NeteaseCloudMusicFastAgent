@echo off
For /f "skip=1 tokens=2 delims=[" %%a in ('ping  music.163.com') do (
        For /f "tokens=1 delims=]" %%b in ("%%a") do (
                Set ip=%%b
        )
)
cd %~dp0
node\node.exe app.js -p 2333 -f %ip%