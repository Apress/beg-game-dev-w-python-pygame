[Setup]
SolidCompression=true
AppName=Ant State Machine
AppVerName=Ant State Machine 1.0
DefaultDirName={pf}\ant state machine
DefaultGroupName=ant state machine
ShowLanguageDialog=yes
[Files]
Source: dist\*.*; DestDir: {app}
[Icons]
Name: {group}\Launch Ants; Filename: {app}\antsstatemachine.exe; WorkingDir: {app}
Name: {group}\Uninstall Ants; Filename: {uninstallexe}
