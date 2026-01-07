#Maintainer: Viking @kasem_shibli <https://twitter.com/kasem_shibli>

pkgname=arsenal
pkgver=1.3.0
pkgrel=1
pkgdesc='Arsenal is just a quick inventory and launcher for hacking programs'
url='https://github.com/kasem545/arsenal'
arch=('any')
license=('GPL')
depends=('python>=3.7')
source=(${pkgname}::git+https://github.com/kasem545/arsenal.git)
sha512sums=('SKIP')

build() {
	cd $pkgname
	python setup.py build
}

package() {
	cd $pkgname

	echo "alias a='arsenal'" >> ~/.bash_aliases
	echo "alias a='arsenal'" >> ~/.zshrc
	echo "alias a='arsenal'" >> ~/.bashrc

	python setup.py install --prefix=/usr --root="${pkgdir}" -O1 --skip-build
	install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}
	install -Dm 644 README.md -t "${pkgdir}"/usr/share/doc/${pkgname}
}
