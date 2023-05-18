#Web stack debuggin 4, change limit
exec { 'change limit to 2000':
  path    => '/bin',
  command => "sed -i 's/15/2000' /etc/default/nginx"
}

-> exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart'
}
