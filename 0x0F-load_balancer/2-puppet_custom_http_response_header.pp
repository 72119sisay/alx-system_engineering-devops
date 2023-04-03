# use puppet to automate the task of creating a custom HTTP header response

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line { 'http_header':
 path => '/etc/nginx/ngnix.conf',
 math => 'http {',
 line => "http {\n\tadd_header x-served-By \"${hostname}\";",
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
