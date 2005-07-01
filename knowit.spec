
%define		_beta beta3

Summary:	KnowIt - a tool for managing notes
Summary(pl):	KnowIt - narzêdzie do zarz±dzania notatkami
Name:		knowit
Version:	0.10
Release:	0.%{_beta}.5
License:	GPL v2
Group:		X11/Applications
%define		_ver	%{version}%{_beta}
Source0:	http://knowit.sourceforge.net/files/%{name}-%{_ver}.tar.bz2
# Source0-md5:	998edb0921fc3b8a1809906f8d530874
Patch0:		%{name}-desktop.patch
URL:		http://knowit.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	libxslt-devel >= 1.0.19
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdebase-core >= 9:3.2.0
Requires:	libxslt >= 1.0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KnowIt is a tool for managing notes.

%description -l pl
KnowIt to rozbudowane narzêdzie do zarz±dzania notatkami.

%prep
%setup -q -n %{name}-%{_ver}
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_desktopdir} \
	kde_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_desktopdir}/{Applications/,}knowit.desktop

echo "Categories=Qt;KDE;Utility;" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/knowit.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/*/*/*/*.png
%{_datadir}/apps/%{name}
%{_datadir}/mimelnk/application/x-knowit.desktop
%{_desktopdir}/knowit.desktop
