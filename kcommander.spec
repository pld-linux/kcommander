%define		_beta		Beta2
Summary:	WindowsCommander-like file manager
Summary(pl):	Zarz±dca plików podobny do Windows Commandera
Name:		kcommander
Version:	3.0
Release:	0.%{_beta}.2
License:	GPL
Group:		X11/Applications
Source0:	ftp://codewizards.de/pub/kcommander/%{name}3-%{version}%{_beta}.tar.gz
# Source0-md5:	70af0c8d114e3813357c031c8c3b3b07
Source1:	http://www.pld-linux.org/Members/andree/%{name}-metal.tar.gz
# Source1-md5:	0bc00f70082a505a86b94ca5115afef0
Patch0:		%{name}-linkfix.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-first-start.patch
URL:		http://www.kcommander.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	qt-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kcommander2

%description
KCommander is the ultimate tool for every ex-windows-users, who used
and liked WindowsCommander.

%description -l pl
KCommander jest narzêdziem s³u¿±cym do zarz±dzania plikami,
przeznaczonym dla by³ych u¿ytkowników Windows, którzy u¿ywali i
polubili Windows Commandera.

%prep
%setup -q -n %{name}3-%{version} -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.* admin
%{__autoconf}
%configure \
	--enable-mt \
	--with-qt-libraries=%{_libdir}

# clean is needed to regenerate files from *.ui for new qt
%{__make} clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/kcommander3
