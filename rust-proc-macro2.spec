# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
# FIXME as of 1.0.70, some tests fail
%bcond_with check
%global debug_package %{nil}

%global crate proc-macro2

Name:           rust-proc-macro2
Version:        1.0.86
Release:        1
Summary:        Substitute implementation of the compiler's proc_macro API to decouple token-based libraries from the procedural macro use case
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/proc-macro2
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(unicode-ident/default) >= 1.0.0 with crate(unicode-ident/default) < 2.0.0~)
BuildRequires:  rust >= 1.56
%if %{with check}
BuildRequires:  (crate(quote) >= 1.0.0 with crate(quote) < 2.0.0~)
BuildRequires:  (crate(rustversion/default) >= 1.0.0 with crate(rustversion/default) < 2.0.0~)
%endif

%global _description %{expand:
A substitute implementation of the compiler's `proc_macro` API to
decouple token-based libraries from the procedural macro use case.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(proc-macro2) = 1.0.70
Requires:       (crate(unicode-ident/default) >= 1.0.0 with crate(unicode-ident/default) < 2.0.0~)
Requires:       cargo
Requires:       rust >= 1.56

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(proc-macro2/default) = 1.0.70
Requires:       cargo
Requires:       crate(proc-macro2) = 1.0.70
Requires:       crate(proc-macro2/proc-macro) = 1.0.70

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(proc-macro2/nightly) = 1.0.70
Requires:       cargo
Requires:       crate(proc-macro2) = 1.0.70

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+proc-macro-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(proc-macro2/proc-macro) = 1.0.70
Requires:       cargo
Requires:       crate(proc-macro2) = 1.0.70

%description -n %{name}+proc-macro-devel %{_description}

This package contains library source intended for building other packages which
use the "proc-macro" feature of the "%{crate}" crate.

%files       -n %{name}+proc-macro-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+span-locations-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(proc-macro2/span-locations) = 1.0.70
Requires:       cargo
Requires:       crate(proc-macro2) = 1.0.70

%description -n %{name}+span-locations-devel %{_description}

This package contains library source intended for building other packages which
use the "span-locations" feature of the "%{crate}" crate.

%files       -n %{name}+span-locations-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
