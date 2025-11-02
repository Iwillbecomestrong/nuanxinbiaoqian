# 自动打包脚本 - 暖心便签弹窗阵列
# 使用方法：在 PowerShell 中运行 .\build.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  暖心便签弹窗阵列 - 自动打包工具" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$pythonExe = "I:\anaconda\python.exe"
$scriptName = "暖心便签弹窗阵列.py"

# 检查 Python 是否存在
if (-not (Test-Path $pythonExe)) {
    Write-Host "❌ 错误：找不到 Python 解释器：$pythonExe" -ForegroundColor Red
    Write-Host "请确认 Anaconda 安装路径是否正确" -ForegroundColor Yellow
    exit 1
}

Write-Host "✓ 找到 Python: $pythonExe" -ForegroundColor Green

# 检查脚本是否存在
if (-not (Test-Path $scriptName)) {
    Write-Host "❌ 错误：找不到脚本文件：$scriptName" -ForegroundColor Red
    exit 1
}

Write-Host "✓ 找到脚本: $scriptName" -ForegroundColor Green
Write-Host ""

# 测试脚本是否能运行
Write-Host "正在测试脚本..." -ForegroundColor Yellow
$testResult = & $pythonExe $scriptName --test
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 脚本测试失败，请检查代码" -ForegroundColor Red
    exit 1
}
Write-Host "✓ 脚本测试通过" -ForegroundColor Green
Write-Host ""

# 检查 PyInstaller 是否已安装
Write-Host "正在检查 PyInstaller..." -ForegroundColor Yellow
$checkPyInstaller = & $pythonExe -m pip show pyinstaller 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "PyInstaller 未安装，正在安装..." -ForegroundColor Yellow
    Write-Host "使用清华镜像源加速下载..." -ForegroundColor Cyan
    
    & $pythonExe -m pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ PyInstaller 安装失败" -ForegroundColor Red
        Write-Host ""
        Write-Host "请尝试以下方法：" -ForegroundColor Yellow
        Write-Host "1. 使用其他镜像源：" -ForegroundColor White
        Write-Host "   $pythonExe -m pip install pyinstaller -i https://mirrors.aliyun.com/pypi/simple/" -ForegroundColor Gray
        Write-Host "2. 手动下载安装包：" -ForegroundColor White
        Write-Host "   访问 https://pypi.org/project/pyinstaller/#files" -ForegroundColor Gray
        Write-Host "3. 查看详细说明：打包说明.md" -ForegroundColor White
        exit 1
    }
}

Write-Host "✓ PyInstaller 已就绪" -ForegroundColor Green
Write-Host ""

# 清理旧的构建文件
Write-Host "正在清理旧的构建文件..." -ForegroundColor Yellow
if (Test-Path "dist") { Remove-Item -Recurse -Force "dist" }
if (Test-Path "build") { Remove-Item -Recurse -Force "build" }
if (Test-Path "*.spec") { Remove-Item -Force "*.spec" }
Write-Host "✓ 清理完成" -ForegroundColor Green
Write-Host ""

# 开始打包
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  开始打包..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

& $pythonExe -m PyInstaller --onefile --noconsole --name "暖心便签弹窗阵列" $scriptName

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ 打包失败" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  ✓ 打包成功！" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "可执行文件位置：" -ForegroundColor Cyan
Write-Host "  $PWD\dist\暖心便签弹窗阵列.exe" -ForegroundColor White
Write-Host ""
Write-Host "使用方法：" -ForegroundColor Cyan
Write-Host "  测试运行（5个弹窗）：" -ForegroundColor White
Write-Host "    .\dist\暖心便签弹窗阵列.exe --test" -ForegroundColor Gray
Write-Host ""
Write-Host "  完整运行（200个弹窗）：" -ForegroundColor White
Write-Host "    .\dist\暖心便签弹窗阵列.exe" -ForegroundColor Gray
Write-Host ""
Write-Host "  自定义弹窗数量：" -ForegroundColor White
Write-Host "    .\dist\暖心便签弹窗阵列.exe --count 50 --stagger 100" -ForegroundColor Gray
Write-Host ""

# 询问是否立即测试
$response = Read-Host "是否立即运行测试？(y/n)"
if ($response -eq "y" -or $response -eq "Y") {
    Write-Host ""
    Write-Host "正在启动测试（5个弹窗）..." -ForegroundColor Yellow
    Start-Process ".\dist\暖心便签弹窗阵列.exe" -ArgumentList "--test"
}

Write-Host ""
Write-Host "完成！" -ForegroundColor Green
