# Puppet manifest to fix a bug in wp-setings.php

exec { 'fix the php extension issue':
  command => 'sed -i 's/phpp/php/g' /var/www/html/index.html',
  path    => '/usr/local/bin/:/bin/'
}
