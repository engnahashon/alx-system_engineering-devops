#Automate install and conf of nginx server
class nginx_setup {
  exec { 'update':
    command => '/usr/bin/apt-get -y update',
  }

  package { 'nginx':
    ensure => installed,
  }

  exec { 'ufw_allow_nginx':
    command => '/usr/sbin/ufw allow "Nginx HTTP"',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "server {\n  listen 80 default_server;\n  listen [::]:80 default_server;\n  add_header X-Served-By \$HOSTNAME;\n  root /var/www/html;\n  index index.html index.htm index.nginx-debian.html;\n  server_name _;\n  location / {\n    try_files \$uri \$uri/ =404;\n  }\n}\n",
  }

  file { '/var/www/html/index.nginx-debian.html':
    ensure  => present,
    content => 'Hello World!',
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => [
      Package['nginx'],
      File['/etc/nginx/sites-available/default'],
      File['/var/www/html/index.nginx-debian.html'],
    ],
  }
}

include nginx_setup
