%define		_beta		Beta2
Summary:	WindowsCommander-like file manager
Summary(pl):	Zarz±dca plików podobny do Windows Commandera
Name:		kcommander
Version:	3.0
Release:	0.%{_beta}.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://codewizards.de/pub/kcommander/%{name}3-%{version}%{_beta}.tar.gz
Patch0:		%{name}-linkfix.patch
URL:		http://www.kcommander.org/
BuildRequires:	autoconf
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel
BuildRequires:	kdenetwork-devel
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
%setup -q -n %{name}3-%{version}
%patch -p1

%build
%{__autoconf}
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/kcommander3
#%%{_datadir}/apps/kcommander3
#%%{_pixmapsdir}/*/*/*/*
