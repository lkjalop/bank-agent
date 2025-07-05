@echo off
echo Starting Git push process...
echo.

echo 1. Initializing Git repository...
git init
if %errorlevel% neq 0 (
    echo ERROR: Git init failed
    pause
    exit /b 1
)
echo OK: Git repository initialized

echo.
echo 2. Adding files to staging...
git add .
if %errorlevel% neq 0 (
    echo ERROR: Git add failed
    pause
    exit /b 1
)
echo OK: Files added to staging

echo.
echo 3. Creating initial commit...
git commit -m "Initial commit: FastAPI Bank Account Agent with Render deployment config"
if %errorlevel% neq 0 (
    echo ERROR: Git commit failed
    pause
    exit /b 1
)
echo OK: Initial commit created

echo.
echo 4. Setting main branch...
git branch -M main
if %errorlevel% neq 0 (
    echo ERROR: Branch rename failed
    pause
    exit /b 1
)
echo OK: Main branch set

echo.
echo 5. Adding remote repository...
git remote add origin https://github.com/lkjalop/bank-agent.git
if %errorlevel% neq 0 (
    echo ERROR: Remote add failed
    pause
    exit /b 1
)
echo OK: Remote repository added

echo.
echo 6. Pushing to GitHub...
git push -u origin main
if %errorlevel% neq 0 (
    echo ERROR: Git push failed - this might be due to authentication
    echo Please check your GitHub credentials
    pause
    exit /b 1
)
echo OK: Code pushed to GitHub successfully!

echo.
echo SUCCESS: All files have been pushed to https://github.com/lkjalop/bank-agent.git
echo.
echo Next steps:
echo 1. Go to https://render.com
echo 2. Click "New Web Service"
echo 3. Connect your GitHub account
echo 4. Select the bank-agent repository
echo 5. Click "Create Web Service"
echo.
echo Your app will be deployed at: https://bank-agent.onrender.com
pause
