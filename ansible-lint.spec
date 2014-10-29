%global archive_name ansible-lint
%global lib_name ansiblelint

Name:           %{archive_name}
Version:        1.0.4
Release:        1%{?dist}
Summary:        Best practices checker for Ansible

License:        MIT
URL:            https://github.com/willthames/ansible-lint
Source0:        https://pypi.python.org/packages/source/a/%{archive_name}/%{archive_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  ansible
Requires:       ansible

%description
Checks playbooks for practices and behavior that could potentially be improved

%prep
%setup -q -n %{archive_name}-%{version}
rm -rf *.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root=%{buildroot}

%files
%doc PKG-INFO LICENSE
%{_bindir}/%{name}
%{python_sitelib}/%{lib_name}
%{python_sitelib}/ansible_lint-%{version}-py2.?.egg-info

%changelog
* Mon Oct 27 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.4-1
- rename to ansible-lint
- new upstream 1.0.4 release which added LICENSE file.

* Sat Oct 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-2
- Better add upstream LICENSE file, not present in tarball

* Wed Sep 24 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-1
- Initial packaging

