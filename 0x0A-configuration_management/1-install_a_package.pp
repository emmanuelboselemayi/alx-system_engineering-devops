# task 1. Install a package

package { 'flask':
  ensure   => '2.1.0',
  provider => gem,
}
