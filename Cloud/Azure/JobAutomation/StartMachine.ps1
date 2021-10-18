#RUN AS ACCOUNT CONNECTION
$connection = Get-AutomationConnection -Name AzureRunAsConnection
Connect-Azaccount -ServicePrincipal -Tenant $connection.TenantID `
-ApplicationID $connection.ApplicationID -CertificateThumbprint $connection.CertificateThumbprint

$rg = "YOUR_RG"
$vms = "YOUR_VM"


foreach ($vm in $vms)
{
    Write-output "starting up VM "$vm""
    Start-AzVM -ResourceGroupName $rg -Name $vm
}