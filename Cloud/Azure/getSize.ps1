# Inicialize o tamanho total em bytes
$totalSizeInBytes = 0

# Liste todas as assinaturas às quais você tem acesso
$subscriptions = Get-AzSubscription

foreach ($subscription in $subscriptions) {
    # Selecione a assinatura atual para trabalhar nela
    Set-AzContext -SubscriptionId $subscription.Id

    Write-Host "Analisando assinatura: $($subscription.Name)"

    # Obtenha todas as instâncias de SQL Server na assinatura atual
    $servers = Get-AzSqlServer

    foreach ($server in $servers) {
        Write-Host "`tAnalisando servidor: $($server.ServerName)"

        # Obtenha todos os bancos de dados para a instância atual do SQL Server
        $databases = Get-AzSqlDatabase -ResourceGroupName $server.ResourceGroupName -ServerName $server.ServerName

        foreach ($database in $databases) {
            # Adicione o tamanho do banco de dados ao total
            $totalSizeInBytes += $database.DatabaseSizeBytes

            # Log do tamanho do banco de dados individual
            $dbSizeInGB = $database.DatabaseSizeBytes / 1GB
            Write-Host "`t\tTamanho do banco de dados $($database.DatabaseName): $($dbSizeInGB.ToString("F3")) GB"
        }
    }
}

# Converta o tamanho total de bytes para gigabytes
$totalSizeInGB = $totalSizeInBytes / 1GB

# Exiba o tamanho total
Write-Host "`nTamanho total de todos os bancos de dados em todas as assinaturas: $($totalSizeInGB.ToString("F3")) GB"
