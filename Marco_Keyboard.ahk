;right ctrl + right alt + num
>^>!1::run "C:\nirtools\ControlMyMonitor" "/ChangeValue" "DELL U2415" "10" -2
>^>!2::send {volume_down}
>^>!3::run "C:\nirtools\ControlMyMonitor" "/ChangeValue" "VA32AQ" "10" -2
>^>!4::run "C:\nirtools\ControlMyMonitor" "/ChangeValue" "DELL U2415" "10" +2
>^>!5::send {volume_up}
>^>!6::run "C:\nirtools\ControlMyMonitor" "/ChangeValue" "VA32AQ" "10" +2
>^>!7::run "C:\nirtools\MultiMonitorTool" "/switch" "\\.\DISPLAY2"
;>^>!8::run DO NOTHING
>^>!9::run "C:\DisableMonitor.exe"