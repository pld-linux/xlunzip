Summary:	Test tool for lzip_decompress Linux kernel module
Summary(pl.UTF-8):	Narzędzie testowe dla modułu jądra Linuksa lzip_decompress
Name:		xlunzip
Version:	0.8
Release:	1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	http://download.savannah.gnu.org/releases/lzip/xlunzip/%{name}-%{version}.tar.lz
# Source0-md5:	f4b1460882a556ea6da18bd5e0e63aec
URL:		http://savannah.nongnu.org/projects/lzip/
BuildRequires:	lzip
BuildRequires:	tar >= 1:1.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xlunzip is a test tool for the lzip_decompress Linux kernel module.
It's similar to lunzip, but it uses lzip_decompress module code as a
backend.

%description -l pl.UTF-8
Xlunzip to narzędzie testowe dla modułu jądra Linuksa lzip_decompress.
Jest podobne do narzędzia lunzip, ale wewnętrznie wykorzystuja kod
modułu lzip_decompress.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xlunzip
%{_mandir}/man1/xlunzip.1*
