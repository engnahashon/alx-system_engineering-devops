#Web stack debuggin 4, change limit
exec { 'change_limit_to_2000':
  path    => '/bin/',
  command => 'sed -i "s/15/2000/" /etc/default/nginx'
}

-> exec { 'restart_nginx':
  command => '/usr/sbin/service nginx restart'
}
