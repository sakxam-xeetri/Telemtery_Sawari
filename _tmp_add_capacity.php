<?php
$f = __DIR__ . '/data/vehicles.json';
$vehicles = json_decode(file_get_contents($f), true);
foreach ($vehicles as &$v) {
    if (!isset($v['capacity'])) {
        $v['capacity'] = 40;
    }
}
unset($v);
file_put_contents($f, json_encode($vehicles, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
echo "Done: added capacity to " . count($vehicles) . " vehicles\n";
