#RUN AS ACCOUNT CONNECTION
$connection = Get-AutomationConnection -Name AzureRunAsConnection
Connect-Azaccount -ServicePrincipal -Tenant $connection.TenantID `
-ApplicationID $connection.ApplicationID -CertificateThumbprint $connection.CertificateThumbprint



Write-output "Starting up VMs"
Start-AzVM -Name "YOUR_VM1"  -ResourcegroupName "YOUR_RG1"
Start-AzVM -Name "YOUR_VM2" -ResourcegroupName "YOUR_RG1"
Start-AzVM -Name "YOUR_VM1" -ResourcegroupName "YOUR_RG2"