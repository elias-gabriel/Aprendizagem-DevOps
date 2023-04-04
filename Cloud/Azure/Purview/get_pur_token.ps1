$tenantID = ""

$url = "https://login.microsoftonline.com/$tenantID/oauth2/token"
$params = @{ client_id = ""; client_secret = ""; grant_type = "client_credentials"; resource = ‘https://purview.azure.net’ }

Invoke-WebRequest $url -Method Post -Body $params -UseBasicParsing | ConvertFrom-Json
