%define		_beta		Beta2
Summary:	File management
Summary(pl):	Menad�er plik�w podobny do Windows Commandera
Name:		kcommander
Version:	3.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://codewizards.de/pub/kcommander/%{name}3-%{version}%{_beta}.tar.gz
URL:		http://www.kcommander.org/
BuildRequires:	autoconf
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel
BuildRequires:	kdenetwork-devel
BuildRequires:	qt-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kcommander2

%define			_prefix		/usr/X11R6

%description
KCommander is the ultimate tool for every ex-windows-users, who used
and liked WindowsCommander.

%description -l pl
KCommander jest narz�dziem s�u��cym do zarz�dzania plikami,
przeznaczonym dla by�ych u�ytkownik�w Windows, kt�rzy u�ywali i
polubili Windows Commandera.

%prep
%setup -q -n %{name}3-%{version}

%build
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/kcommander3
%{_datadir}/apps/kcommander3
#%{_pixmapsdir}/*/*/*/*
