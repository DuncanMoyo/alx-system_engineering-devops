#  automating the creation of a custom HTTP header response, but with Puppet

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  add_header X-Served-By \$hostname;
  location / {
    root /var/www/html;
    index index.html;
  }
}",
  require => Package['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

