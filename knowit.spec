%define		_beta beta1
Summary:	KnowIt - a tool for managing notes
Summary(pl):	KnowIt - narzêdzie do zarz±dzania notatkami
Name:		knowit
Version:	0.8
Release:	0.%{_beta}.1
License:	GPL v2
Group:		X11/Applications
%define		_ver	%{version}%{_beta}
Source0:	http://knowit.sourceforge.net/files/%{name}-%{_ver}.tar.bz2
URL:		http://knowit.sourceforge.net/
BuildRequires:	kdelibs-devel  >= 3.0
BuildRequires:	libxslt-devel >= 1.0.19
BuildRequires:	qt-devel > 3.0 
Requires:	kdebase >= 3.0
Requires:	libxslt >= 1.0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
KnowIt is a tool for managing notes.

%description -l pl
KnowIt to rozbudowane narzêdzie do zarz±dzania notatkami.

%prep
%setup -q -n %{name}-%{_ver}

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure --enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities
mv $RPM_BUILD_ROOT%{_applnkdir}/Applications/knowit.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%find_lang %{name}  --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*/*/*/*.png
%{_datadir}/apps/%{name}
%{_applnkdir}/Utilities/knowit.desktop
