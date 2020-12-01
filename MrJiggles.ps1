Clear-Host
echo "Mr Jiggles"

echo "+------------+"
echo "|            |"
echo "| +---+      |"
echo "| |   | +--+ |"
echo "| |   | |  | |"
echo "| +---+ +--+ |"
echo "|            |"
echo "| X        X |"
echo "| X       XX |"
echo "| XX      X  |"
echo "|  XXXXXXXX  |"
echo "|            |"
echo "|            |"
echo "+-----X------+"
echo "      X"
echo "      X"
echo "     XX"
echo "     X"
echo "   +---+"
echo "   |   |"
echo "   |   |"
echo "   +---+"
echo "Jiggley Wiggley..."

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