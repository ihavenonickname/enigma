Push-Location ..\src\

Write-Output ENIGMA | python program.py `
    --reflector "B" `
    --rotor1 "I A" `
    --rotor2 "II A" `
    --rotor3 "III A"

Write-Output AAA | python program.py `
    --reflector "B" `
    --rotor1 "I M" `
    --rotor2 "II I" `
    --rotor3 "III U"

Write-Output AAA | python program.py `
    --reflector "B" `
    --rotor1 "I M" `
    --rotor2 "II I" `
    --rotor3 "III U" `
    --plugboard "ZA" `
    --plugboard "PQ" `
    --plugboard "JK"

Pop-Location
