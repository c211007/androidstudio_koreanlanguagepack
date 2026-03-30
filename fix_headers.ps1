# Script to fix .properties file headers
# Removes decorative box headers and replaces with simple comments

$messagesDir = "src\main\resources\messages"
$files = Get-ChildItem -Path $messagesDir -Filter "*_ko.properties"

$fixedCount = 0
$skippedCount = 0

foreach ($file in $files) {
    Write-Host "Processing: $($file.Name)"
    
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    
    # Check if file has decorative header
    if ($content -match '(?s)^# ╔.*?# ╚[^\n]*\n') {
        # Extract the bundle name from filename
        $bundleName = $file.Name -replace '_ko\.properties$', '.properties'
        
        # Get current date
        $date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        
        # Create simple header
        $simpleHeader = @"
# Auto-generated Korean translation file
# Generated: $date
# Original file: $bundleName

"@
        
        # Remove decorative header (from start to after ╚ line, including blank lines)
        $newContent = $content -replace '(?s)^# ╔.*?# ╚[^\n]*\n+', $simpleHeader
        
        # Write back to file
        $newContent | Set-Content -Path $file.FullName -Encoding UTF8 -NoNewline
        
        Write-Host "  ✓ Fixed: $($file.Name)" -ForegroundColor Green
        $fixedCount++
    }
    else {
        Write-Host "  - Skipped (no decorative header): $($file.Name)" -ForegroundColor Yellow
        $skippedCount++
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  Fixed: $fixedCount files" -ForegroundColor Green
Write-Host "  Skipped: $skippedCount files" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
