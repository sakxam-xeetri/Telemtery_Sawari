<?php
// Sawari Landing Page
$envFile = __DIR__ . '/.env';
$env = [];
if (file_exists($envFile)) {
  foreach (file($envFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) as $line) {
    if (str_starts_with(trim($line), '#')) continue;
    if (strpos($line, '=') === false) continue;
    [$key, $value] = explode('=', $line, 2);
    $env[trim($key)] = trim($value);
  }
}
$groqApiKey = $env['GROQ_API_KEY'] ?? '';
include __DIR__ . '/landing1.html';
