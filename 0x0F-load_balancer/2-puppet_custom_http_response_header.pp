#  automating the creation of a custom HTTP header response, but with Puppet

class nginx_custom_header {
  package { 'nginx':
    ensure => 'installed',
  }

  file { '/etc/nginx/conf.d/custom-header.conf':
    ensure  => 'present',
    content => "server_tokens off;\nadd_header X-Served-By ${::hostname};",
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure => 'running',
    enable => true,
  }
}

include nginx_custom_header
