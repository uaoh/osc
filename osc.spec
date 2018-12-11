# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       osc

# >> macros
# << macros

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
Summary:    OpenSUSE Build Service Commander
Version:    0.146.0
Release:    2
Group:      Development/Tools/Other
License:    GPL v2 or later
BuildArch:  noarch
URL:        http://www.gitorious.org/opensuse/osc
Source0:    osc-%{version}.tar.bz2
Source100:  osc.yaml
Patch0:     0001-Add-sb2install-support-to-osc.patch
Patch1:     0002-Support-osc-copyprj-in-api-by-Islam-Amer.patch
Patch2:     0003-Support-synchronous-copyproj.patch
Patch3:     0004-Add-p-to-copyprj-to-enable-copying-of-prjconf.patch
Patch4:     0005-Add-support-for-rebuild-and-chroot-only-in-build.patch
Patch5:     0006-Add-architecture-and-scheduler-maps.patch
Patch6:     0007-Trap-any-kind-of-exception-during-plugin-parsing-eg-.patch
Patch7:     0008-Fixup-old-style-print-statements.patch
Requires:   python-urlgrabber
Requires:   m2crypto > 0.19
Requires:   /usr/bin/less
Requires:   /usr/bin/diff3
BuildRequires:  python-devel
BuildRequires:  python-urlgrabber
BuildRequires:  m2crypto

%description
Commandline client for the openSUSE Build Service.

See http://en.opensuse.org/Build_Service/CLI , as well as
http://en.opensuse.org/Build_Service_Tutorial for a general
introduction.


%prep
%setup -q -n src

# 0001-Add-sb2install-support-to-osc.patch
%patch0 -p1
# 0002-Support-osc-copyprj-in-api-by-Islam-Amer.patch
%patch1 -p1
# 0003-Support-synchronous-copyproj.patch
%patch2 -p1
# 0004-Add-p-to-copyprj-to-enable-copying-of-prjconf.patch
%patch3 -p1
# 0005-Add-support-for-rebuild-and-chroot-only-in-build.patch
%patch4 -p1
# 0006-Add-architecture-and-scheduler-maps.patch
%patch5 -p1
# 0007-Trap-any-kind-of-exception-during-plugin-parsing-eg-.patch
%patch6 -p1
# 0008-Fixup-old-style-print-statements.patch
%patch7 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%{__python} setup.py install --root=%{buildroot} -O1

# >> install post
ln -s osc-wrapper.py %{buildroot}/%{_bindir}/osc
mkdir -p %{buildroot}/var/lib/osc-plugins
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 0755 dist/complete.csh %{buildroot}%{_sysconfdir}/profile.d/osc.csh
install -m 0755 dist/complete.sh %{buildroot}%{_sysconfdir}/profile.d/osc.sh
%if 0%{?suse_version} > 1110
mkdir -p %{buildroot}%{_prefix}/lib/osc
install -m 0755 dist/osc.complete %{buildroot}%{_prefix}/lib/osc/complete
%else
mkdir -p %{buildroot}%{_prefix}/%{_lib}/osc
install -m 0755 dist/osc.complete %{buildroot}%{_prefix}/%{_lib}/osc/complete
%endif
# << install post

%check
(
    cd tests
    python suite.py
)

%files
%defattr(-,root,root,-)
# >> files
%{_bindir}/osc*
%{python_sitelib}/*
%{_sysconfdir}/profile.d/*
%if 0%{?suse_version} > 1110
%dir %{_prefix}/lib/osc
%{_prefix}/lib/osc/*
%else
%dir %{_prefix}/%{_lib}/osc
%{_prefix}/%{_lib}/osc/*
%endif
%dir /var/lib/osc-plugins
%doc AUTHORS README TODO NEWS
%doc %_mandir/man1/osc.*
# << files
