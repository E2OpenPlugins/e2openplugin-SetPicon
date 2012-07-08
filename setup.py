from distutils.core import setup
import setup_translate

pkg = 'Extensions.SetPicon'
setup (name = 'enigma2-plugin-extensions-setpicon',
       version = '0.36',
       description = 'work with services picons',
       packages = [pkg],
       package_dir = {pkg: 'plugin'},
       package_data = {pkg: ['*.xml', '*/*.png', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass = setup_translate.cmdclass, # for translation
      )
