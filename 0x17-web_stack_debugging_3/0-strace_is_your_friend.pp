# Fixing the issue

exec { 'right path':
    cwd => '/var/www/html/',
    command => 'sed -i "s/.phpp/.php/g"  /var/www/html/wp-settings.php'
}
