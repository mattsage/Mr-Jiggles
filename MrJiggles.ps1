Clear-Host
echo "Mr Jiggles"
echo "#####################")
echo "Mr Jiggles")
echo "#####################")
echo "+------------+")
echo "|             |")
echo "| +---+       |")
echo "| |   |  +--+ |")
echo "| |   |  |  | |")
echo "| +---+  +--+ |")
echo "|             |")
echo "| X         X |")
echo "| X        XX |")
echo "| XX       X  |")
echo "|  XXXxXXXXX  |")
echo "|             |")
echo "|             |")
echo "+-----[]------+")
echo "      []")
echo "      [][]")
echo "        []")
echo "        []")
echo "      +----+")
echo "      |    |")
echo "      |[][]|")
echo "      +----+")


Add-Type -AssemblyName System.Windows.Forms
$PlusOrMinus = 1
while ($true)
{
  $p = [System.Windows.Forms.Cursor]::Position
  $x = $p.X + $PlusOrMinus
  $y = $p.Y + $PlusOrMinus
  [System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
  Start-Sleep -Seconds 180
  $PlusOrMinus *= -1
}
