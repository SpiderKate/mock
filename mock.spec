Summary: Builds packages inside chroots
Name: mock
Version: 0.4
Release: 1
License: GPL
Group: Development/Tools
Source: http://fedoraproject.org/projects/mock/releases/%{name}-%{version}.tar.gz
URL: http://fedoraproject.org/wiki/Projects/Mock
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: python, yum >= 2.2.1
Requires(pre): shadow-utils
BuildRequires: libselinux-devel


%description
Mock takes a srpm and builds it in a chroot

%prep
%setup -q

%build
make


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
# make the default.cfg link
cd $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
ln -s fedora-development-i386-core.cfg default.cfg


%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ $1 -eq 1 ]; then
    groupadd -r mock >/dev/null 2>&1 || :
fi



%files
%defattr(-, root, root)
%doc README ChangeLog
%dir  %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*.cfg
%{_bindir}/%{name}
%{_libexecdir}/mock-yum
%{_mandir}/man1/mock.1*
%attr(04750, root, mock) %{_sbindir}/mock-helper
%attr(02775, root, mock) %dir /var/lib/mock
%{_libdir}/libselinux-mock.so


%changelog
* Tue Dec 27 2005 Seth Vidal <skvidal@phy.duke.edu>
- add patch from Andreas Thienemann - adds man page

* Sat Jun 11 2005 Seth Vidal <skvidal@phy.duke.edu>
- security fix in mock-helper

* Sun Jun  5 2005 Seth Vidal <skvidal@phy.duke.edu>
- clean up packaging for fedora extras

* Thu May 19 2005 Seth Vidal <skvidal@phy.duke.edu>
- second packaging and backing down the yum ver req

* Sun May 15 2005 Seth Vidal <skvidal@phy.duke.edu>
- first version/packaging
