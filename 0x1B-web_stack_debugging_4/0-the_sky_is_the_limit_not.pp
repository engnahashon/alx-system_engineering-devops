#Web stack debuggin 4, change limit
exec { 'change limit to 5000':
  path    => '/bin',
  command => "sed -i 's/15/5000' /etc/default/nginx"
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart'
}
