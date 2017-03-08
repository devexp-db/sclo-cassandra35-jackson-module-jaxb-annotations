%{?scl:%scl_package jackson-module-jaxb-annotations}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}jackson-module-jaxb-annotations
Version:	2.7.6
Release:	3%{?dist}
Summary:	JAXB annotations support for Jackson (2.x)
License:	ASL 2.0
URL:		http://wiki.fasterxml.com/JacksonJAXBAnnotations
Source0:	https://github.com/FasterXML/%{pkg_name}/archive/%{pkg_name}-%{version}.tar.gz

BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix}jackson-annotations
BuildRequires:	%{?scl_prefix}jackson-core
BuildRequires:	%{?scl_prefix}jackson-databind
BuildRequires:	%{?scl_prefix}jackson-parent
BuildRequires:	%{?scl_prefix}replacer
BuildRequires:	%{?scl_prefix}jsr-311
BuildRequires:	%{?scl_prefix}fasterxml-oss-parent
# do not require jaxb-api dependency in scl package
%{!?scl:BuildRequires:	mvn(javax.xml.bind:jaxb-api)}
%{?scl:Requires: %scl_runtime}

BuildArch:	noarch

%description
Support for using JAXB annotations as an alternative to
"native" Jackson annotations, for configuring data binding.

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}

cp -p src/main/resources/META-INF/LICENSE .
cp -p src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
# remove jaxb-api dependency in scl package
%{?scl:%pom_remove_dep :jaxb-api}

%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README.md release-notes/*
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Wed Mar 08 2017 Tomas Repik <trepik@redhat.com> - 2.7.6-3
- scl conversion

* Tue Feb 07 2017 Michael Simacek <msimacek@redhat.com> - 2.7.6-2
- Regenerate BuildRequires

* Mon Aug 22 2016 gil cattaneo <puntogil@libero.it> 2.7.6-1
- update to 2.7.6

* Fri Jun 24 2016 gil cattaneo <puntogil@libero.it> 2.6.7-1
- update to 2.6.7

* Thu May 26 2016 gil cattaneo <puntogil@libero.it> 2.6.6-1
- update to 2.6.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 25 2015 gil cattaneo <puntogil@libero.it> 2.6.3-1
- update to 2.6.3

* Mon Sep 28 2015 gil cattaneo <puntogil@libero.it> 2.6.2-1
- update to 2.6.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 31 2015 gil cattaneo <puntogil@libero.it> 2.5.0-1
- update to 2.5.0

* Sat Sep 20 2014 gil cattaneo <puntogil@libero.it> 2.4.2-1
- update to 2.4.2

* Fri Jul 04 2014 gil cattaneo <puntogil@libero.it> 2.4.1-1
- update to 2.4.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.2.2-4
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 gil cattaneo <puntogil@libero.it> 2.2.2-2
- review fixes

* Tue Jul 16 2013 gil cattaneo <puntogil@libero.it> 2.2.2-1
- 2.2.2
- renamed jackson-module-jaxb-annotations

* Tue Jul 16 2013 gil cattaneo <puntogil@libero.it> 2.2.1-1
- 2.2.1

* Wed Oct 24 2012 gil cattaneo <puntogil@libero.it> 2.1.0-1
- update to 2.1.0
- renamed jackson2-module-jaxb-annotations

* Thu Sep 13 2012 gil cattaneo <puntogil@libero.it> 2.0.5-1
- initial rpm
