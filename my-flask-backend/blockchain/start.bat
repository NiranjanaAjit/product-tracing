start cmd /k ganache-cli -p 9545
start cmd /k ganache-cli -p 9090

timeout /t 10 /nobreak >nul


start cmd /k truffle migrate --network development
start cmd /k truffle migrate --network development9090