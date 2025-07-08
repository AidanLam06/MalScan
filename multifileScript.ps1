<#
.SYNOPSIS
    Automates file scanner program, allowing user to run the program iteratively through a folder
.DESCRIPTION
    User can input a folder path as a parameter for this script file (ran through CLI) and run the main program iteratively through the folder to scan multiple files at once
#>

param (
    [string]$FolderPath,
    [string]$ApiKey
)

if (-not $FolderPath) {
    $FolderPath = Read-Host "Enter folder path"
}
if (-not $ApiKey) {
    $ApiKey = Read-Host "Enter MalwareBazaar API key"
}
if (-not (Test-Path -Path $FolderPath)) {
    Write-Error "Folder does not exist or the location you specified does not contain a folder with that name"
    exit 1
}

$items = Get-ChildItem -Path $FolderPath -Recurse

$batchSize = 50
$processed = 0

$detected = @{}
$unhandled = [System.Collections.ArrayList]@()

foreach ($batch in $items | Select-Object -Skip $processed -First $batchSize | Select-Object -ExpandProperty FullName) {
    $batch | ForEach-Object {
        try {
            $string = python main.py --file $_ --apikey $ApiKey 2>&1
            $result = ($string -split "-", 2)[0].Trim()
            $color = ($string -split "-", 2)[1].Trim()

            if (-not ($LASTEXITCODE -eq 0)) {
                Write-Host "[ERROR] $_" -ForegroundColor Red
                [void]$unhandled.Add($_)
            }
            else {
                Write-Host "[$result]" -ForegroundColor $color  
                if ($color -ne "Green") {
                    detected[$_] = $string
                }
            }
            $processed++
        }
        catch {
            Write-Host "[FATAL ERROR] $_" -ForegroundColor Red
            [void]$unhandled.Add($_)
        }
    }
}

$maxPathLength = ($detected.Keys | Measure-Object -Property Length -Maximum).Maximum

Write-Host "********LIST OF DETECTED FILES********"
Write-Host ("{0} : {1}" -f "File Path".PadRight($maxPathLength), "Risk")
Write-Host("{0} : {1}" -f "---------".PadRight($maxPathLength), "----")

foreach ($entry in $detected.GetEnumerator()) {
    $riskPieces = $entry.Value -split "-"
    $risk = riskPieces[0]
    $color = $riskPieces[1]

    $paddedPath = $entry.Key.PadRight($maxPathLength)

    Write-Host -NoNewline $paddedPath
    Write-Host -NoNewline " : "
    Write-Host $risk -ForegroundColor $color
}

Write-Host "********LIST OF UNHANDLED FILES********"
$unhandled | ForEach-Object {Write-Host $_}
Write-Host "`nScan complete. Processed $processed files." -ForegroundColor Cyan