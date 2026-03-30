#!/usr/bin/env python3
"""Generate concubro Open Graph cards as PNG files.

This script is intentionally tiny and Windows-oriented: it shells out to
PowerShell and uses .NET's System.Drawing so the repo does not need extra
Python packages.
"""

from __future__ import annotations

import argparse
import subprocess
import textwrap
from pathlib import Path


def ps_single_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def title_font_size(title: str) -> int:
    length = len(title.strip())
    if length <= 22:
        return 82
    if length <= 32:
        return 76
    if length <= 42:
        return 70
    return 64


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a concubro OG image.")
    parser.add_argument("--title", required=True, help="Main card title")
    parser.add_argument("--description", required=True, help="Synopsis text")
    parser.add_argument("--output", required=True, help="Output PNG path")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent
    assets_dir = repo_root / ".assets"
    output_path = (repo_root / args.output).resolve()

    powershell = textwrap.dedent(
        f"""
        Add-Type -AssemblyName System.Drawing
        $ErrorActionPreference = 'Stop'

        function New-RoundedRectPath([float]$x,[float]$y,[float]$w,[float]$h,[float]$r) {{
          $path = New-Object System.Drawing.Drawing2D.GraphicsPath
          $d = $r * 2
          $path.AddArc($x, $y, $d, $d, 180, 90)
          $path.AddArc($x + $w - $d, $y, $d, $d, 270, 90)
          $path.AddArc($x + $w - $d, $y + $h - $d, $d, $d, 0, 90)
          $path.AddArc($x, $y + $h - $d, $d, $d, 90, 90)
          $path.CloseFigure()
          return $path
        }}

        function Wrap-Text([System.Drawing.Graphics]$g, [string]$text, [System.Drawing.Font]$font, [float]$maxWidth) {{
          $words = $text -split '\\s+'
          $lines = New-Object System.Collections.Generic.List[string]
          $current = ''
          foreach ($word in $words) {{
            $candidate = if ($current) {{ "$current $word" }} else {{ $word }}
            $size = $g.MeasureString($candidate, $font)
            if ($size.Width -le $maxWidth -or -not $current) {{
              $current = $candidate
            }} else {{
              $lines.Add($current)
              $current = $word
            }}
          }}
          if ($current) {{ $lines.Add($current) }}
          return ,$lines.ToArray()
        }}

        $width = 1200
        $height = 630
        $bg = [System.Drawing.ColorTranslator]::FromHtml('#e0ddca')
        $fg = [System.Drawing.ColorTranslator]::FromHtml('#111111')
        $white = [System.Drawing.ColorTranslator]::FromHtml('#f7f3e8')

        $fonts = New-Object System.Drawing.Text.PrivateFontCollection
        $fonts.AddFontFile({ps_single_quote(str((assets_dir / "raleway-200.ttf").resolve()))})
        $fonts.AddFontFile({ps_single_quote(str((assets_dir / "raleway-400.ttf").resolve()))})
        $fonts.AddFontFile({ps_single_quote(str((assets_dir / "playfair-display.ttf").resolve()))})

        $raleway = $fonts.Families | Where-Object {{ $_.Name -eq 'Raleway' }} | Select-Object -First 1
        $ralewayLight = $fonts.Families | Where-Object {{ $_.Name -eq 'Raleway ExtraLight' }} | Select-Object -First 1
        $playfair = $fonts.Families | Where-Object {{ $_.Name -eq 'Playfair Display' }} | Select-Object -First 1

        $bmp = New-Object System.Drawing.Bitmap $width, $height
        $g = [System.Drawing.Graphics]::FromImage($bmp)
        $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
        $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
        $g.Clear($bg)

        $fgBrush = New-Object System.Drawing.SolidBrush($fg)
        $whiteBrush = New-Object System.Drawing.SolidBrush($white)
        $blackBrush = New-Object System.Drawing.SolidBrush($fg)

        $logoPath = New-RoundedRectPath 84 64 124 124 26
        $g.FillPath($blackBrush, $logoPath)
        $logoFont = New-Object System.Drawing.Font($raleway, 48, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
        $logoFormat = New-Object System.Drawing.StringFormat
        $logoFormat.Alignment = [System.Drawing.StringAlignment]::Center
        $logoFormat.LineAlignment = [System.Drawing.StringAlignment]::Center
        $g.DrawString('no', $logoFont, $whiteBrush, (New-Object System.Drawing.RectangleF(84, 64, 124, 124)), $logoFormat)

        $brandFont = New-Object System.Drawing.Font($ralewayLight, 44, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
        $g.DrawString('concubro', $brandFont, $fgBrush, 274, 98)

        $title = {ps_single_quote(args.title)}
        $desc = {ps_single_quote(args.description)}
        $titleFont = New-Object System.Drawing.Font($raleway, {title_font_size(args.title)}, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
        $descFont = New-Object System.Drawing.Font($playfair, 44, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)

        $titleLines = Wrap-Text $g $title $titleFont 1020
        $y = 214
        foreach ($line in $titleLines) {{
          $g.DrawString($line, $titleFont, $fgBrush, 80, $y)
          $y += 84
        }}

        $descLines = Wrap-Text $g $desc $descFont 1020
        $y = 414
        foreach ($line in $descLines) {{
          $g.DrawString($line, $descFont, $fgBrush, 80, $y)
          $y += 54
        }}

        $bmp.Save({ps_single_quote(str(output_path))}, [System.Drawing.Imaging.ImageFormat]::Png)

        $logoPath.Dispose(); $logoFormat.Dispose(); $logoFont.Dispose(); $brandFont.Dispose(); $titleFont.Dispose(); $descFont.Dispose()
        $fgBrush.Dispose(); $whiteBrush.Dispose(); $blackBrush.Dispose(); $g.Dispose(); $bmp.Dispose(); $fonts.Dispose()
        """
    ).strip()

    subprocess.run(
        ["powershell", "-NoProfile", "-Command", powershell],
        check=True,
        cwd=repo_root,
    )


if __name__ == "__main__":
    main()
